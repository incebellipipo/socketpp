#include <iostream>
#include <tcp-server/tcp-server.hpp>

int main() {

  server::TcpServer tcpServer;

  try {
    tcpServer.initialize();
  } catch (std::exception &e){
    std::cerr << e.what() << std::endl;
    tcpServer.destroy();
  }

  return 0;
}