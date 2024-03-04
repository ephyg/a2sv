class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        count=Counter(senate)
        letter=[i for i in senate]
        banD=0
        banR=0
        if len(count)==1:
            if senate[0]=="D":
                return "Dire"
            return "Radiant"
        for i,let in enumerate(letter):
            if let=="R":
                if banR>0:
                    banR-=1
                elif banR==0:
                    banD+=1
                    count["D"]-=1
                    letter.append("R")
            if let=="D":
                if banD>0:
                    banD-=1
                elif banD==0:
                    banR+=1
                    count["R"]-=1
                    letter.append("D")
            if count["R"]==0 or count["D"]==0:
                break
        if count["D"]>0:
            return "Dire"
        else:
            return "Radiant"

                
                
        return "a"