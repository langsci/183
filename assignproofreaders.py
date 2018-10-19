import sys
from datetime import datetime, date, time, timedelta


githubid = sys.argv[1] 

template = """Dear  {name},
thanks for your offer. The book can be found at
https://paperhive.org/documents/remote?type=langsci&id={githubid} 

You are assigned the following chapters:
{chapterlist}

Please also have a look at the lists of references, in particular missing capitalization.

Next to the Paperhive online annotation platform, you can also download the pdf from http://langsci.github.io/{githubid}/proofreading.pdf if you prefer. Having the correction at Paperhive in a central place has proven much more convenient for the authors, but it is up to you to choose your preferred method of proofreading.

Guidelines for proofreaders can be found here
http://langsci-press.org/public/downloads/LangSci_Guidelines_Proofreaders.pdf

For most of the issues mentioned there, native competence is not necessary. We have every chapter checked by 2 people, at least one of which is a native speaker.

We aim at having the corrections in by {duedate}. Please let us know when you are done. 

Best wishes and thanks again for your help
Sebastian
"""

chapters = ['0']+[l.strip() for l in open("chapternames").readlines()]
assignments = open("assignments").readlines()

mails = []

for a in assignments:
	name = a.split()[0]
	chapternumbers = a.split()[1:]
	chapterlist = '\n'.join("* %s %s"%(i,chapters[int(i)]) for i in chapternumbers)	
	mails.append(template.format(name=name,   
			      chapterlist=chapterlist, 
			      githubid=githubid,
			      duedate=(datetime.now() + timedelta(weeks=4)).strftime("%B %d")))
	
separator =	'\n'+80*'-'+'\n'
print separator.join(mails)
