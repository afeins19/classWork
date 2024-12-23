#include <stdio.h>

#include <unistd.h>

#include <string.h> // lets us get the len of a string 

#include <sys/wait.h> // waiting so no one reads an empty buffer 


int main() {

    int pipe_fd[2]; // allocate space for file descriptors for ends of the pipes


    // creating the pipe within the if statement 

    if(pipe(pipe_fd) == -1){

        perror("\t\nFailed to Create Pipe!");

    }

    // creating a child processes

    pid_t pid = fork(); 


    // testing if child was made
    if(pid == -1){

        perror("\t\nFailed to Fork!\n");

    }

    else if (pid == 0){

        printf("\nForking Successful!\n");

        printf("----------------------------\n");

    }


    // parent process 

    if(pid > 0){

        char parent_msg[] = "[Parent] Hello my child!"; // setting char-array for parent msg

        write(pipe_fd[1], parent_msg, strlen(parent_msg) + 1); // writing msg to pipe 

        

        wait(NULL); // wait for child to finish 

        char child_rsp[40]; // allocate buffer for child to respond

        read(pipe_fd[0], child_rsp, sizeof(child_rsp)); //read in data from pipe



        // child finished, message waiting in pipe 

        printf("\t[Parent] Recieved Msg from Child: %s\n\n", child_rsp);

        

        // closing r/w of the pipe after getting message back 

        close(pipe_fd[1]);

        close(pipe_fd[0]);



    } else if(pid == 0) { // child process

       

        // allocate space for parent message

        char buffer[50];

        read(pipe_fd[0], buffer, sizeof(buffer)); // read from read-end of pipe into buffer

        

        printf("\t[Child] Recieved Msg from Parent: %s\n", buffer);



        // -- Child response --

        char child_msg[] = "[Child] Hello parent, this is child!";

        write(pipe_fd[1], child_msg, strlen(child_msg) + 1); // send message back to parent 

        

        // closing write pipe

        close(pipe_fd[1]); 

        return 0; // child tells parent its done 

    }



    return 0; 

}