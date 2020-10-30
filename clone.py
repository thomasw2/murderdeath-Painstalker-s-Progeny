import random
#murderdeath painstalker

def main():
	random.seed()
	words=[[] for i in range(4)]
	words[0]=["slayer","murder","assassin","bloodshed","crime","destruction",\
			"felony","homicide","lynch","manslaughter","massacre","terrorizer",\
			"annihilation","blood","butchery","carnage","death","foulplay"]
	words[1]=["annililation","destructor","dying","eradicator","exterminator",\
				"finisher","heaven","oblivion","ruin","reaper"]
	words[2]=["ache","agony","burn","cramp","misery","sick","sore","spasm",\
				"strain","tender","torment","trouble","wound","hurt","gripe",\
			"sting","torture","anguish","anxiety","bitter","grief","sad","suffer",\
			"woe","wrack","pain"]
	words[3]=["stalker","chaser","hunter","maker","grasp"]
	name=""
	for i in range(4):
		if i==2:
			name+=" "
		chosen=words[i][random.randint(0,len(words[i])-1)]
		name+=chosen
	print(name)

if __name__=="__main__":
	main()
