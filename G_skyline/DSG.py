################################
#2016/10/24 22:13
#Divis Wen  
################################
import time

class point:
	def __init__(self,point_id,point_coordination):
		self.layer=0
		self.parent_id_set=set()
		self.child_id_set=set()
		self.id=point_id
		self.coordination=point_coordination
		self.layer_location=0

class DSG:
	def __readFile(self,datapath,N):
		f=open(datapath,'r')
		lines=f.readlines()
		raw_list=[]
		for ii in range(1, N):
			line = lines[ii]
		#for line in lines:
			p=[]
			for i in line.split():
				p.append(float(i))
			raw_list.append(p)
		sorted_list=sorted(raw_list,key=lambda p:p[0])
		index=0
		self.point_list=[]
		for item in sorted_list:
			new_point=point(index,item)
			self.point_list.append(new_point)
			index+=1

	def __isDominated(self,point_1,point_2):
		mark=False
		dim_size=len(point_1.coordination)
		for i in range(dim_size):
			if point_1.coordination[i]>point_2.coordination[i]:
				return False
			elif point_1.coordination[i]<point_2.coordination[i]:
				mark=True
		return mark

	def __isWithin(self,point,layer_index):
		time_is=time.clock()
		if not self.is2Dim:
			for edge_point in self.layer_dict[layer_index]:
				if self.__isDominated(edge_point,point):
					self.within_time+=time.clock()-time_is
					return True
			self.within_time+=time.clock()-time_is
			return False
		else:
			if self.__isDominated(self.layer_dict[layer_index][-1],point):
				self.within_time+=time.clock()-time_is
				return True
			self.within_time+=time.clock()-time_is
			return False

	def __findCandidateSet(self,current_layer):
		candidate_id_list=[]
		while(current_layer>1):
			current_layer-=1
			for p in self.layer_dict[current_layer]:
				candidate_id_list.append(p.id)
		return candidate_id_list

	def __layerConstructor(self):	
		#constructing layers
		i=1
		while(i<len(self.point_list)):
			layer_index=self.maxlayer
			while(layer_index>=1):
				is_within=self.__isWithin(self.point_list[i],layer_index) 
				if is_within and layer_index==self.group_size:
					break
				elif is_within:
					self.maxlayer=max(layer_index+1,self.maxlayer)
					self.layer_dict[layer_index+1].append(self.point_list[i])
					self.DSG_point_dict[i]=self.point_list[i]
					self.DSG_point_dict[i].layer=layer_index+1
					self.DSG_point_dict[i].layer_location=len(self.layer_dict[layer_index+1])-1
					break
				layer_index-=1
			if layer_index==0:
				self.layer_dict[layer_index+1].append(self.point_list[i])
				self.DSG_point_dict[i]=self.point_list[i]
				self.DSG_point_dict[i].layer=layer_index+1
				self.DSG_point_dict[i].layer_location=len(self.layer_dict[layer_index+1])-1

			i+=1
			#if i%1000==0:
			#	print float(i)/float(len(self.point_list))

	def __init__(self, datapath, group_size, N):
		#print filename,group_size
		#num of points in one group
		self.within_time=0
		self.group_size=group_size

		#layer_dict: recording points in each layer
		#{layer_index:[point1,point2,....]} layer_index=1,2,3,...,group_size
		self.layer_dict=dict()
		for i in range(self.group_size):
			self.layer_dict[i+1]=[]

		#DSG_point_dict: record all point in DSG (all points in first group_size layers) 
		#{point_id: point}
		self.DSG_point_dict=dict()

		#dimension mark used by ___isWithin()
		self.is2Dim=True

		#list restoring all points in the file.
		self.point_list=[]
		self.__readFile(datapath, N)

		#initialization
		self.point_list[0].layer=1
		self.maxlayer=1
		self.layer_dict[1].append(self.point_list[0])
		self.DSG_point_dict[0]=self.point_list[0]
		if len(self.point_list[0].coordination)>2:
			self.is2Dim=False

		time_2=time.clock()
		
		#constructing layers
		self.__layerConstructor()
		
		#print '2',time.clock()-time_2
		time_3=time.clock()
		
		#constructing DSG
		i=self.maxlayer
		counter=0
		while(i>1):
			for p in self.layer_dict[i]:
				for candidate_id in self.__findCandidateSet(i):
					counter+=1
					if self.__isDominated(self.DSG_point_dict[candidate_id],p):
						self.DSG_point_dict[candidate_id].child_id_set.add(p.id)
						self.DSG_point_dict[p.id].parent_id_set.add(candidate_id)
			i-=1

