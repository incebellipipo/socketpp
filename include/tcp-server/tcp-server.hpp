#pragma once
#ifndef TCP_SERVER_HPP_
#define TCP_SERVER_HPP_

#include <sys/types.h>
#include <exception>
#include <stdexcept>

namespace server {
  class TcpServer {
  protected:
    int listen_fd_;
    u_int16_t port_;

    int buffer_size_ = 10;

    void create();

    void closeSocket(int fd);

    void serve();

    void handle(int client_fd);

    std::string get_request(int client_fd);

    void send_response(int client_fd, char *response);

  public:
    TcpServer(u_int16_t port = 12345);

    void destroy();


    void initialize();

  };

  class TcpServerException : public std::exception {
  public:
    explicit TcpServerException(const char* message) : msg_(message) {}
    explicit TcpServerException(const std::string& message) : msg_(message) {}
    ~TcpServerException() final = default;
    const char* what() const noexcept final { return msg_.what(); }
  protected:
    std::runtime_error msg_;
  };
}

#endif
