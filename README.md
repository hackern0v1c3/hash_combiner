# hash_combiner
Takes a file of username:hash and a file of hash:Password.  Outputs a list of username:password

# formatting tips
Here are some examples to take output from popular programs and format it for hash_combiner.  Please send other examples and I can post them here.

1. secretsdump.py : cat secrets_dump.txt |cut -d'\' -f2 | cut -d':' -f1,4 > secrets_dump_reformated.txt
