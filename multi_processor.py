from link import node
from link import linked_list
import time
class task:
	def __init__(self,n,rd,cpu):
		self.n=n
		self.rd=rd
		self.cpu=cpu

	def create_job(self,n,at):
		return job(n,self.n,self.rd,self.cpu,at)

class job:
	def __init__(self,no,task_no,rd,cpu,at):
		self.no=no
		self.task_no=task_no
		self.rd=rd
		self.cpu=cpu
		self.cpucpy=cpu
		self.at=at
		self.abd=at+rd
		self.finish=-1

def feasiblity(jobs):
	sum=0
	for i in jobs:
		sum=sum+float(i.cpu/i.abd)
	return sum

def main():
	t=0
	#task_types=[task(0,5,2),task(1,8,3),task(2,15,5),task(3,20,6),task(4,22,5)]
	#job_table=[task_types[0].create_job(0,0),task_types[1].create_job(1,0),task_types[3].create_job(2,1),task_types[2].create_job(3,2),task_types[0].create_job(4,3),task_types[4].create_job(5,5),task_types[1].create_job(6,6)]
	#task_types=[task(0,5,1),task(1,10,3),task(2,15,2),task(3,20,5),task(4,25,5)]
	#job_table=[task_types[0].create_job(0,0),task_types[1].create_job(1,0),task_types[3].create_job(2,1),task_types[2].create_job(3,2),task_types[0].create_job(4,3),task_types[4].create_job(5,5),task_types[1].create_job(6,6),task_types[2].create_job(7,7),task_types[0].create_job(8,8),task_types[4].create_job(9,9)]
	task_types=[task(0,2,1),task(1,6,3),task(2,8,2),task(3,10,5),task(4,15,5)]
	job_table=[task_types[1].create_job(0,0),task_types[0].create_job(1,1),task_types[3].create_job(2,2),task_types[2].create_job(3,3),task_types[2].create_job(4,3),task_types[4].create_job(5,5)]
	copy_table=job_table[:]
	ready_queue=linked_list()
	processor_list=[None for i in range(3)]
	#print("Feasiblity = ",feasiblity(job_table))
	#ti=time.time()
	while not isEmpty(ready_queue) or job_table !=[] or not isEmpty_P(processor_list):
		if t == 0:
			while job_table != [] and job_table[0].at==0:
				job = job_table[0]
				ready_queue.append(job)
				job_table.pop(0)
			for i in range(len(processor_list)):
				#print("ready queue",isEmpty(ready_queue))
				if isEmpty(ready_queue):
					break
				processor_list[i]=ready_queue.remove()
				#print(processor_list)
			#print(processor_list)ready_queue.print()
		elif job_table!=[] and job_table[0].at==t:
			while job_table!=[] and job_table[0].at==t:
				job=job_table.pop(0)
				index=find_process(processor_list)
				if index != None:
					temp=node(job)
					processor_list[index]=temp
				else:
					index=max_process(processor_list)
					if job.abd<processor_list[index].val.abd:
						temp=processor_list[index].val
						processor_list[index].val=job
						if temp.cpu>0:
							ready_queue.insert_head(temp)
					else:
						pos=ready_queue.findpos(job) #implement this
		print("at time ",t)
		if not isEmpty_P(processor_list):
			for i  in range(len(processor_list)):
				if processor_list[i] != None and processor_list[i].val.cpu>0:
					print(processor_list[i].val.no)
					processor_list[i].val.cpu=processor_list[i].val.cpu-1
					if processor_list[i].val.cpu==0:
						processor_list[i].val.finish=t+1
				else:
					if not isEmpty(ready_queue):
						processor_list[i]=ready_queue.remove()
						processor_list[i].val.cpu=processor_list[i].val.cpu-1
						print(processor_list[i].val.no)
					else:
						processor_list[i]=None
		t=t+1
	#print("Time taken to Execute : ",time.time()-ti," seconds")
	table(copy_table)

def isEmpty(ready_queue):
	if ready_queue.head==None:
		return True
	else:
		return False

def isEmpty_P(processor_list):
	for i in processor_list:
		if i != None:
			return False
	return True

def find_process(processor_list):
	for i in range(len(processor_list)):
		if processor_list[i] == None:
			return i
	return None

def max_process(processor_list):
	maxx=processor_list[0].val.cpu
	index=0
	for i in range(len(processor_list)):
		if processor_list[i].val.cpu > maxx:
			index=i
			maxx=processor_list[i].val.cpu
	return index

def table(job_table):
	print("\nJob-Table :\n")
	print("Job No.\t Arrival-Time  CPU-Time  Absolute-Deadline  Finish-Time")
	for i in job_table:
		print("  ",i.no,"\t     ",i.at,"\t ",i.cpucpy,"\t\t",i.abd,"\t\t",i.finish)
			
main()