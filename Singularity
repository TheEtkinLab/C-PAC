Bootstrap: docker
From: fcpindi/c-pac
IncludeCmd: yes

%help
You are in the C-PAC container. To see help run
singularity run TheEtkinLab-C-PAC.simg -h

%runscript
    echo "Running C-PAC!"
    echo "Arguments received: $*"
    exec /code/run.py "$@"

%labels
Author mnarayan@users.noreply.github.com
Build-date 19/01/2019
Vendor Ubuntu
Version 1.3.0

%post

ln -s /usr/lib/x86_64-linux-gnu/libgsl.so.19.0.0 \
      /usr/lib/x86_64-linux-gnu/libgsl.so.19

ln -s /usr/lib/x86_64-linux-gnu/libgsl.so.19.0.0 \
      /usr/lib/x86_64-linux-gnu/libgsl.so.0

if [ -e /usr/lib/x86_64-linux-gnu/libGL.so.1 ] ; then
    rm -f /usr/lib/x86_64-linux-gnu/libGL.so.1
fi

ln -s /usr/lib/x86_64-linux-gnu/mesa/libGL.so.1.2.0 \
   /usr/lib/x86_64-linux-gnu/libGL.so.1
   
echo "Hello from inside the C-PAC container"
echo "Install additional software here"
