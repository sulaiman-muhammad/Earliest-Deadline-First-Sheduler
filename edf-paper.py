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
		self.at=at
		self.abd=at+rd
		self.cpucpy=cpu
		self.finish=-1

def feasiblity(jobs):
	sum=0
	for i in jobs:
		sum=sum+float(i.cpu/i.abd)
	return sum
         
def main():
    t=0
    no_task=5
    task_types=[task(0,5,2),task(1,8,3),task(2,15,5),task(3,20,6),task(4,22,5)]
    job_table=[task_types[0].create_job(0,0),task_types[1].create_job(1,0),task_types[3].create_job(2,1),task_types[2].create_job(3,2),task_types[0].create_job(4,3),task_types[4].create_job(5,5),task_types[1].create_job(6,6)]
    #task_types=[task(0,5,1),task(1,10,3),task(2,15,2),task(3,20,5),task(4,25,5)]
    #job_table=[task_types[0].create_job(0,0),task_types[1].create_job(1,0),task_types[3].create_job(2,1),task_types[2].create_job(3,2),task_types[0].create_job(4,3),task_types[4].create_job(5,5),task_types[1].create_job(6,6),task_types[2].create_job(7,7),task_types[0].create_job(8,8),task_types[4].create_job(9,9)]
    #task_types=[task(0,2,1),task(1,6,3),task(2,8,2),task(3,10,5),task(4,15,5)]
    #job_table=[task_types[1].create_job(0,0),task_types[0].create_job(1,1),task_types[3].create_job(2,2),task_types[2].create_job(3,3),task_types[2].create_job(4,3),task_types[4].create_job(5,5)]
    copy_table=job_table[:]
    ready_queue=[[0,linked_list()] for i in range(5)]
    process=None
    flag=1
    flag1=1
    #print("Feasiblity = ",feasiblity(job_table))
    #ti=time.ti
    while isEmpty(ready_queue) or flag==1 or flag1==1 or job_table != []:
        flag=0
        #print("0")
        if t==0:
            #print("1")
            while job_table!=[] and job_table[0].at==0:
                job=job_table[0]
                ready_queue[job.task_no][0]=1
                ready_queue[job.task_no][1].insert_head(job)
                job_table.pop(0)
            l=least_setbit(ready_queue) 
            process=ready_queue[l][1].remove()
            if ready_queue[l][1].head==None:
                ready_queue[l][0]=0
        elif job_table!=[] and job_table[0].at==t:
            while job_table!=[] and job_table[0].at==t:
                job=job_table[0]
                if job.abd < process.val.abd:
                    temp=process.val
                    process.val=job
                    job=temp
                    l=least_setbit(ready_queue)
                    if l!=None:
                        p=min(job.task_no,least_setbit(ready_queue))
                    else:
                        p=job.task_no
                    if job.cpu>0:
                        ready_queue[p][1].insert_head(job)
                        ready_queue[p][0]=1
                else:
                    h=next_list(job.task_no,ready_queue)
                    #print(h,"H")
                    if h!=-1:
                        last=ready_queue[h][1].tail
                        while last!=None and last.val.abd<job.abd:
                            if ready_queue[job.task_no][1].head==None:
                                ready_queue[job.task_no][1].head=ready_queue[h][1].head
                                ready_queue[job.task_no][1].tail=ready_queue[h][1].tail
                                ready_queue[job.task_no][0]=1
                            else:
                                ready_queue[job.task_no][1].tail.nxt=ready_queue[h][1].head
                                ready_queue[job.task_no][1].tail=ready_queue[h][1].tail
                            ready_queue[h][1].head=None
                            ready_queue[h][1].tail=None
                            ready_queue[h][0]=0
                            h=next_list(job.task_no,ready_queue)
                            #work in prog
                            #print(h,"h")
                            last=ready_queue[h][1].tail
                            #print(last,"h")
                        while ready_queue[h][1].head!=None and ready_queue[h][1].head.val.abd<job.abd:
                            temp=ready_queue[h][1].remove()
                            if ready_queue[job.task_no][1].head==None:
                                ready_queue[job.task_no][1].insert_head(temp)
                                ready_queue[job.task_no][0]=1
                            else:
                                ready_queue[job.task_no][1].tail.next=temp
                                ready_queue[job.task_no][1].tail=temp
                        if ready_queue[job.task_no][1].head==None:
                            ready_queue[job.task_no][1].insert_head(job)
                            ready_queue[job.task_no][0]=1
                        else:
                            temp=node(job)
                            ready_queue[job.task_no][1].tail.nxt=temp
                            ready_queue[job.task_no][1].tail=temp
                        
                    else:
                        if ready_queue[job.task_no][1].head==None:
                            ready_queue[job.task_no][1].insert_head(job)
                            ready_queue[job.task_no][0]=1
                        else:
                            temp=node(job)
                            ready_queue[job.task_no][1].tail.nxt=temp
                            ready_queue[job.task_no][1].tail=temp
                              
                job_table.pop(0)
        print("at time ",t)
        if process.val.cpu<1:
            l=least_setbit(ready_queue)
            if l==None:
                flag1=0
            else:
                process=ready_queue[l][1].remove()
                if ready_queue[l][1].head==None:
                    ready_queue[l][0]=0
                process.val.cpu=process.val.cpu-1
                print(process.val.no)
                if process.val.cpu==0:
                	process.val.finish=t+1
        else:
            process.val.cpu=process.val.cpu-1
            if process.val.cpu==0:
            	process.val.finish=t+1
            print(process.val.no)
        t=t+1
    #print("Time taken to Execute : ",time.time()-ti," seconds")
    table(copy_table)

def isEmpty(ready_queue):
    for i in ready_queue:
        if i[0]==1:
            return True
    return False

def least_setbit(ready_queue):
    for i in range(len(ready_queue)):
        if ready_queue[i][0]==1:
            return i
    return None

def next_list(k,ready_queue):
    for i in range(k+1,len(ready_queue),1):
        if ready_queue[i][0]==1:
            return i
    return -1

def table(job_table):
	print("\nJob-Table :\n")
	print("Job No.\t Arrival-Time  CPU-Time  Absolute-Deadline  Finish-Time")
	for i in job_table:
		print("  ",i.no,"\t     ",i.at,"\t ",i.cpucpy,"\t\t",i.abd,"\t\t",i.finish)

main()
