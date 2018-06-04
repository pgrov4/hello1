print(".bollywood movie")

live=5;
print("you have five lives")
right=0
while(live>0):
    movie="raazi"
    l=len(movie)
    print("5 letter alia bhatt movie?")
    print("you have",+live,"lives")
    print("_ _ _ _ _")
    ans=input("enter letter in lower case")
    if ans in movie:
        print("right, next character?")
        right=right+1;
        print(right,"characters right")
        if(right==l):
            print("you got it right")
            print("movie is raazi")
            exit(0)
    else:
        live=live-1;
#if(right==len):
 #   print("great!!! you won")
if(live==0):
    print("you have lost your lives")
    print("movie was raazi")
