#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <errno.h>

#define BUFSIZE 1024
#define DestIp "xx.xx.xx.xx"
#define DestPort 9000
#define Req "GET /index.html HTTP/1.1\r\nHost: xx.xx.xx.xx\r\nConnection: Close\r\n\r\n"
#define ReqLen sizeof(Req)

int main(int argc, char *argv[]) {
                ssize_t i;
                int nRequestLen;

                char strResponse[BUFSIZE]={0};
                char strRequest[BUFSIZE]={0};


                int sockfd, numbytes;
                struct sockaddr_in dest_addr; /* connector's address information */

                if ((sockfd = socket(AF_INET, SOCK_STREAM, 0)) == -1) {
                                perror("socket");
                                exit(1);
                }

                dest_addr.sin_family = AF_INET; /* host byte order */
                dest_addr.sin_port = htons(DestPort); /* short, network byte order */
                dest_addr.sin_addr.s_addr = inet_addr(DestIp);

                /* Create and setup the connection */
                if (connect(sockfd, (struct sockaddr *)&dest_addr,sizeof(struct sockaddr)) == -1){
                                perror("connect");
                                exit(1);
                }

                /* Send the request */
                strncpy(strRequest, Req,ReqLen);
                nRequestLen = ReqLen;
                if (write(sockfd,strRequest,nRequestLen) == -1) {
                        perror("write");
                        exit(1);
                }

                /* Read in the response */
                while(1) {
                                i = read(sockfd,strResponse,BUFSIZE-1);
                                if(0 >= i){
                                                break;
                                }
                                strResponse[i]='\0';
                                printf(strResponse);

                }

                /* Close the connection */
                close(sockfd);
}