Docker: Package for what to install. Has dependdenices in it
 packages are identical. Deploy them. solves oh it works on my machine problem.
 Package up eveything the app needs to run. works the smae

 packages are individual . without any coordination.
 kubernters comes here for coordination

 Kubernteres control plane decides how many packages, wjere to deploy, auto replaces the failed containers, and coordiantrs the whole operation

 Kubernters control plane : API server : takes orders, scheduler : which server to load, controller : keep it running
 
 Worker nodes ( virtual severs) : serve1 - database, sevrer2 - db, sever3 -  streaming wtc...

  The app code                                            
  - The exact runtime it needs (Python 3.11, Node 18, etc.)                                                                                                                       
  - Its dependencies (pip install, npm install)            
  - Its config

  - Docker engine
  - virtulazie the OS. share the smae kernel
  - Dokcer file : code , the image : builds the code and spins the container, the contianer
  start from a templaetae image
FROM : pulss the image from the cloud
RUN : run a terminal command, install dependencis
ENV env variables
CMD : default command that executes when you start up a command

Container is a layersd of images. At the bottom we have linux , and that leads upto the application image
dockerfile: This is how you build it

My problem is writting and intution. I am not good enough or i dont know how to do this yet. i am lazy as fuck to commit to wriritng code. but working make
s the dopamine hit

 
 
