Open the binary in IDA. Identify the __call_me function. Replace `call validate_hash` by `call __call_me`. Set a breakpoint on `get_hash_string`. Give any input and continue until you hit the breakpoint inside `__call_me`. You should see the flag passed as an argument to the hashing function. 

![](call_me_sol.png)
