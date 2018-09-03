#include <socketpp/socketpp.hpp>
#include <sys/ioctl.h>
#include <cstdlib>
#include <sys/socket.h>
#include <cerrno>
#include <iostream>
#include <cstring>
#include <unistd.h>
#include <fcntl.h>


namespace socketpp {
  void Socketpp::send_all(int fd, char *data) {
    // prepare to send response
    unsigned long nleft = strlen(data);
    int nwritten;

    int error = 0;
    socklen_t len = sizeof (error);
    int retval = getsockopt (fd, SOL_SOCKET, SO_ERROR, &error, &len);

    if (retval != 0) {
      /* there was a problem getting the error code */
      std::cerr << "Error getsockopt() #1 " << std::string(strerror(errno)) << std::endl;
      std::cerr << "Error getsockopt() #2 " << std::string(strerror(error)) << std::endl;
      return;
    }

    // loop to be sure it is all sent
    int total_written = 0;
    while (nleft) {
      if ((nwritten = (int) send(fd, &data[total_written], nleft, 0)) < 0) {
        total_written += nwritten;
        if (errno == EINTR) {
          // the socket call was interrupted
          continue;
        } else if ( errno == ECONNRESET) {
          // connection reset by peer
          std::cerr << "Error send() " << std::string(strerror(errno)) << std::endl;
          return;
        } else {
          // an error occurred, so break out
          std::cerr << "Error send() " << std::string(strerror(errno)) << std::endl;
          return;
        }

      } else if (nwritten == 0) {
        return;
      }
      nleft -= nwritten;
    }
  }

  int Socketpp::read_all(int fd, char *&data) {
    int bytes_in_buffer = -1;

    ioctl(fd, FIONREAD, &bytes_in_buffer);

#ifndef BUFFER_SIZE
#define BUFFER_SIZE 128
#endif

    char buffer[BUFFER_SIZE] = {0};

    if( bytes_in_buffer > 0 ){

      size_t total_chars = 0;
      ssize_t chars_read;

      do {

        bzero(buffer, BUFFER_SIZE);
        chars_read = recv(fd, buffer,(size_t)BUFFER_SIZE - 1, 0);
        total_chars += chars_read;

        if( chars_read < 0){
          if(errno == EINTR){
            continue;
          } else if (errno == ENETRESET){
            std::cerr << "Error recv(): " << std::string(strerror(errno)) << std::endl;
          } else {
            std::cerr << "Error recv(): " << std::string(strerror(errno)) << std::endl;
            break;
          }
        }

        // reallocate memory to fit the request
        char *hold_data = nullptr;
        hold_data = (char*) realloc(data, total_chars * sizeof(char));
        data = hold_data;
        // concatenate strings
        strcat(data, buffer);

        // if we read less than we want, than there is nothing to read
        if( chars_read < BUFFER_SIZE){
          ioctl(fd, FIONREAD, &bytes_in_buffer);
          if(bytes_in_buffer == 0){
            break;
          }
        }

      } while( chars_read > 0);

      return (int)total_chars;
    }
  }

  int Socketpp::destroy_fd(int fd) {
    if(fd >= 0) {
      int err = 1;
      socklen_t len = sizeof(err);

      if( getsockopt(fd, SOL_SOCKET, SO_ERROR, (char*)&err, &len) < 0 ){
        std::cerr << "Error getsockopt() #1: " + std::string(strerror(errno)) << std::endl;
        std::cerr << "Error getsockopt() #2: " + std::string(strerror(errno)) << std::endl;
      }

      if(err){
        errno = err;
      }

      if( shutdown( fd, SHUT_WR) < 0){
        if(errno != ENOTCONN && errno != EINVAL){
          std::cerr << "Error shutdown() : " << std::string(strerror(errno)) << std::endl;
        }
      }
      int chunk_size;
      char buffer[128];
      do{
        ioctl(fd, FIONREAD, &chunk_size);
        if(chunk_size > 0){
          read(fd, buffer, 128);
        }
        std::cout << "chunk size: " <<chunk_size << std::endl;
      } while(chunk_size != 0);

      if( shutdown( fd, SHUT_RDWR) < 0){
        if(errno != ENOTCONN && errno != EINVAL){
          std::cerr << "Error shutdown() : " << std::string(strerror(errno)) << std::endl;
        }
      }

      if( close(fd) < 0 ){
        std::cout << "Error close(): " << std::string(strerror(errno)) << std::endl;
      }
    }
  }
}
