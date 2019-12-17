#include <bits/stdc++.h>

using namespace std;

int main(){
	freopen("in", "r", stdin);
	char fluff[4];
	int pc;
	scanf("%s %d",fluff, &pc);
	int opCodes[1000], As[1000], Bs[1000], Cs[10000];
	int nCommands = 0;
	char tOp[5];
	while(scanf("%s %d %d %d", tOp, &As[nCommands], &Bs[nCommands], &Cs[nCommands]) == 4){
		if(strcmp(tOp, "addr")==0){
			opCodes[nCommands]=0;
		} else if (strcmp(tOp, "addi")==0){
			opCodes[nCommands]=1;
		} else if (strcmp(tOp, "mulr")==0){
			opCodes[nCommands]=2;
		} else if (strcmp(tOp, "muli")==0){
			opCodes[nCommands]=3;
		} else if (strcmp(tOp, "banr")==0){
			opCodes[nCommands]=4;
		} else if (strcmp(tOp, "bani")==0){
			opCodes[nCommands]=5;
		} else if (strcmp(tOp, "borr")==0){
			opCodes[nCommands]=6;
		} else if (strcmp(tOp, "bori")==0){
			opCodes[nCommands]=7;
		} else if (strcmp(tOp, "setr")==0){
			opCodes[nCommands]=8;
		} else if (strcmp(tOp, "seti")==0){
			opCodes[nCommands]=9;
		} else if (strcmp(tOp, "gtir")==0){
			opCodes[nCommands]=10;
		} else if (strcmp(tOp, "gtri")==0){
			opCodes[nCommands]=11;
		} else if (strcmp(tOp, "gtrr")==0){
			opCodes[nCommands]=12;
		} else if (strcmp(tOp, "eqir")==0){
			opCodes[nCommands]=13;
		} else if (strcmp(tOp, "eqri")==0){
			opCodes[nCommands]=14;
		} else if (strcmp(tOp, "eqrr")==0){
			opCodes[nCommands]=15;
		}
		nCommands++;
	}
	
	int regs[6];
	
	set<int> possibleValues;
	bool part1 = false;
	int lastInserted = -1;
	while(regs[pc] >= 0 && regs[pc] < nCommands){
		int opCode = opCodes[regs[pc]], A = As[regs[pc]], B= Bs[regs[pc]], C= Cs[regs[pc]];
		if(regs[pc]==28){
			if(!part1){
				printf("%d\n", regs[3]);
				part1 = true;
			}
			bool insertSucess = possibleValues.insert(regs[3]).second;
			if(!insertSucess){
				printf("%d\n", lastInserted);
				break;
			}
			lastInserted = regs[3];
		}
		switch(opCode){
			case 0:
				regs[C] = regs[A] + regs[B];
				break;
			case 1:
				regs[C] = regs[A] + B;
				break;
			case 2:
				regs[C] = regs[A] * regs[B];
				break;
			case 3:
				regs[C] = regs[A] * B;
				break;
			case 4:
				regs[C] = regs[A] & regs[B];
				break;
			case 5:
				regs[C] = regs[A] & B;
				break;
			case 6:
				regs[C] = regs[A] | regs[B];
				break;
			case 7:
				regs[C] = regs[A] | B;
				break;
			case 8:
				regs[C] = regs[A];
				break;
			case 9:
				regs[C] = A;
				break;
			case 10:
				regs[C] = A > regs[B]?1:0;
				break;
			case 11:
				regs[C] = regs[A] > B?1:0;
				break;
			case 12:
				regs[C] = regs[A]>regs[B]?1:0;
				break;
			case 13:
				regs[C] = A == regs[B]?1:0;
				break;
			case 14:
				regs[C] = regs[A] == B?1:0;
				break;
			case 15:
				regs[C] = regs[A] == regs[B]?1:0;
				break;
		}
		
		regs[pc]++;
	}
}
