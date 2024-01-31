/*
    This program will demonstrate the use of the following functions:
        - fork(): this creates a child process from the parent process
        - getpid(): this gets the PID for the child process
        - getppid(): this gets the PID for the parent process of the child 

        Forking: 
            when fork is called, a child process will be created. From the lecture,
            Unix-sytems use the copy-on-write technique which does not duplicate memory pages
            until the child process decides to enact some change. 

        Wait:
            if we dont wait for the child process to execute before killing the parent, 
            we will end up with orphan processes which might get messy, especailly for 
            larger programs. 
*/


#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h> // include for wait()

int main() {
    // allocating space for pid type variables 
    pid_t initial_pid = getpid(); 
    pid_t pid;  

    printf("\n\t\t --- Homework 4: Processes ---");
    printf("\n\nInitial PID [%lu]\n\n", (unsigned long)initial_pid);

    for (int i = 0; i < 3; i++) {
        pid = fork(); // creating a child process from the parent 

        if (pid == 0) {
            // pid is 0 => child process
            printf("\tChild Process | PID [%lu] | PARENT PID [%lu]\n", (unsigned long)getpid(), (unsigned long)getppid());
            
            return 0; // exit to prevent child processes forking unwanted subprocesses 
        } else if (pid > 0) {
            // Otherwise its a parent process
            printf("Parent Process | PID [%lu] | Spawned Child [%lu]\n", (unsigned long)getpid(), (unsigned long)pid);
            wait(NULL); // wait for child process to finish
        } else {
            // forking failed :(
            perror("fork failed");
            return 1;
        }
    }

    return 0;
}

