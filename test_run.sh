#!/bin/bash
source .venv/bin/activate
cd grabber

for i in {1..5}
do
   echo "Round: $i"

   echo "grabber_one_thread.py" >>wyniki.txt
   python grabber_one_thread.py >>wyniki.txt
   
   echo "grabber_multi_threads.py" >>wyniki.txt
   python grabber_multi_threads.py >>wyniki.txt
   
   echo "grabber_multi_processes.py" >>wyniki.txt
   python grabber_multi_processes.py >>wyniki.txt
done

deactivate
