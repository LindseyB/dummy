import random
import os

q=lambda z:''.join([v,v+''.join(random.choice(list(map(chr,range(768,815))))for i in range(int(random.normalvariate(10,5))))][v.isalpha()]for v in z)

messages=[
	"initial commit",
	"update readme.md",
	"update",
	"first commit",
	"dummy",
	"updated readme",
	"pi push",
	"create readme.md",
	"fix",
	"cleanup",
	"test",
	"typo",
	"fuck",
	"wip",
	"bump version",
	"updates"	
]

for n in range(random.randint(1, 10)):
	message = q(random.choice(messages))
	os.system(f'git commit -m "{message}" --allow-empty')
