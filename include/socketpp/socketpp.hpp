#pragma once
#ifndef SOCKETPP_HPP_
#define SOCKETPP_HPP_

namespace socketpp {

  class Socketpp {
  public:
    static int read_all(int fd, char *&data);

    static void send_all(int fd, char *data);

    static int destroy_fd(int fd);
  };

}

#endif //MULTITHREADSOCKETSERVER_SOCKET_HPP
