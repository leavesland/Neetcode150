class Solution:

    def encode(self, strs: List[str]) -> str:
        answer=""
        for i in strs:
            length=len(i)
            word=f"{length}#{i}"
            answer=answer+word
        print(answer)
        return answer
    
    def decode(self, s: str) -> List[str]:
        answer=[]
        while s!="":
            number=""
            for i in s:
                if i!="#":
                    number=number+i
                else:
                    break
            print(number)
            strnumber = len(number)
            number=int(number)
            answer.append(s[strnumber+1:strnumber+1+number])
            s=s[strnumber+1+number:]
        return answer