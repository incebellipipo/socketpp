#include <tcp-server/tcp-server.hpp>
#include <netinet/in.h>
#include <cstring>
#include <iostream>
#include <unistd.h>
#include <sys/ioctl.h>
#include <socketpp/socketpp.hpp>
#include <fcntl.h>
#include <thread>

namespace server {
  TcpServer::TcpServer(u_int16_t port) :
    port_(port)
  {

  }

  void TcpServer::initialize() {
    create();
    serve();
  }

  void TcpServer::destroy() {
    closeSocket(listen_fd_);
  }


  void TcpServer::create(){
    struct sockaddr_in server_addr = {};
    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(port_);
    server_addr.sin_addr.s_addr = htonl(INADDR_ANY);

    listen_fd_ = socket(AF_INET, SOCK_STREAM, IPPROTO_IP);
    if( !listen_fd_ ){
      throw(TcpServerException("Error server(): " + std::string(strerror(errno))));
    }

    int one = 1;
    setsockopt(listen_fd_, SOL_SOCKET, SO_REUSEADDR, (char*)&one, sizeof(int));

    if( bind(listen_fd_, (const struct sockaddr *) & server_addr, sizeof(server_addr)) < 0 ){
      throw(TcpServerException("Error bind(): " + std::string(strerror(errno))));
    }

    int status = fcntl(listen_fd_, F_GETFD, 0);
    if (status >= 0)
      status = fcntl(listen_fd_, F_SETFD, status | FD_CLOEXEC);
    if (status < 0)
      std::cerr << "Error getting/setting socket FD_CLOEXEC flags: " << std::string(strerror(errno)) << std::endl;

    if(listen(listen_fd_, SOMAXCONN) < 0){
      closeSocket(listen_fd_);
      throw(TcpServerException("Error listen(): " + std::string(strerror(errno))));
    }

  }

  void TcpServer::closeSocket(int fd) {
    socketpp::Socketpp::destroy_fd(fd);

  }

  void TcpServer::serve() {

    while(true){
      int client;
      struct sockaddr_in client_addr = {};
      socklen_t client_len = sizeof(client_addr);
      client = accept(listen_fd_, (struct sockaddr*)&client_addr, &client_len);

      std::cout << "Connection accepted. fd: " << client << std::endl;
      if(client < 0){
        throw(TcpServerException("Error accept(): " + std::string(strerror(errno))));
      }
      std::thread handle_thread(&TcpServer::handle, this, client);
      handle_thread.detach();
    }
  }

  void TcpServer::handle(int client_fd) {

    auto request = get_request(client_fd);

    printf("Got: %s\n", request);

    send_response(client_fd, "");

    socketpp::Socketpp::destroy_fd(client_fd);
  }

  char * TcpServer::get_request(int client_fd) {
    char* data = nullptr;
    if( socketpp::Socketpp::read_all(client_fd, data) < 0 ){
      std::cerr << "No data is read." << std::endl;
    }
    return data;
  }

  void TcpServer::send_response(int client_fd, char *response) {
    return socketpp::Socketpp::send_all(client_fd, response);
  }


}