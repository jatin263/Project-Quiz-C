#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<time.h>
#include<unistd.h>
#include<conio.h>
char examQuestion(char q[],int s){
	int f=60;
	char a;
	do{
		printf("\n\t\t\tTime Left :- %d\t\tScore:- %d\n",f,s);
		printf("%s",q);
		printf("Your ans:");
		f--;
		sleep(1);
		system("cls");
	}while(f>0 && !kbhit());
	if(f==0){
		return '0';
	}
	else{
		printf("\n\t\t\tTime Left :- %d\t\tScore:- %d\n",f,s);
		printf("%s",q);
		printf("Your ans:");
		getchar();
		scanf("%c",&a);
		return a;
	}
	
}
int main(){
	int ch;
	char ans;
	int score=0;
	char answer[20]={'a','b','b','b','d','b','b','a','a','a','d','a','c','a','b','a','b','a','b','c'};
	char ques[20][1000]={
	"\n1.Grand Central Terminal, Park Avenue, New York is the world\'s\n(a)largest railway station\n(b)highest railway station\n(c)longest railway station\n(d)None of the above\n",
	"\n2.Entomology is the science that studies\n(a)Behavior of human beings\n(b)Insects\n(c)The origin and history of technical and scientific terms\n(d)The formation of the rocks\n",
	"\n3.Eritrea, which became the 182nd member of the UN in 1993, is in the continent of\n(a)Asia\n(b)Africa\n(c)Europe\n(d)Australia\n",
	"\n4.Garampani sanctuary is located at\n(a)Junagarh, Gujarat\n(b)Diphu, Assam\n(c)Kohima, Nagaland\n(d)Gangtok, Sikkim\n",
	"\n5.For which of the following disciplines is Nobel Prize awarded?\n(a)Physics and Chemistry\n(b)Physiology or Medicine\n(c)Literature, Peace and Economics\n(d)All of the above\n",
	"\n6.Hitler party which came into power in 1933 is known as\n(a)Labour Party\n(b)Nazi Party\n(c)Ku-Klux-Klan\n(d)Democratic Party\n",
	"\n7.FFC stands for\n(a)Foreign Finance Corporation\n(b)Film Finance Corporation\n(c)Federation of Football Council\n(d)None of the above\n",
	"\n8.Fastest shorthand writer was\n(a)Dr. G. D. Bist\n(b)J.R.D. Tata\n(c)J.M. Tagore\n(d)Khudada Khan\n",
	"\n9.Epsom (England) is the place associated with\n(a)Horse racing\n(b)Polo\n(c)Shooting\n(d)Snooker\n",
	"\n10.First human heart transplant operation conducted by Dr. Christiaan Barnard on Louis Washkansky, was conducted in\n(a)1967\n(b)1968\n(c)1958\n(d)1922\n",
	"\n11.Which one is the smallest ocean in the world? \n(a)Indian\n(b)Pacific\n(c)Atlantic\n(d)Arctic\n",
	"\n12. What is the capital of France?\n(a) Paris\n(b) Berlin\n(c) Madrid\n(d) London\n",
	"\n13.Which planet in our solar system is known as the Red Planet?\n(a) Jupiter\n(b) Saturn\n(c) Mars\n(d) Venus\n",
	"\n14. What is the largest country in the world by land area?\n(a) Russia\n(b) China\n(c) United States\n(d) Canada\n",
	"\n15. Who wrote the famous novel To Kill a Mockingbird?\n(a) Ernest Hemingway\n(b) Harper Lee\n(c) F. Scott Fitzgerald\n(d) J.D. Salinger\n",
	"\n16. What is the tallest mammal in the world?\n(a) Giraffe\n(b) Elephant\n(c) Rhino\n(d) Hippopotamus\n",
	"\n17. Who is the founder of Microsoft?\n(a) Steve Jobs\n(b) Bill Gates\n(c) Jeff Bezos\n(d) Mark Zuckerberg\n",
	"\n18. What is the smallest country in the world?\n(a) Vatican City\n(b) Monaco\n(c) San Marino\n(d) Liechtenstein\n",
	"\n19. Which country gifted the Statue of Liberty to the United States?\n(a) Italy\n(b) France\n(c) Spain\n(d) United Kingdom\n",
	"\n20. Who painted the famous artwork The Mona Lisa?\n(a) Vincent van Gogh\n(b) Claude Monet\n(c) Leonardo da Vinci\n(d) Pablo Picasso\n"
	};
	do{
		printf("**************************\t\n\tWELCOME\t\n**************************\n");
		printf("Do you want to play the quiz If YES press 1 If NO then press 2");
		printf("\nEnter your choice:");
		scanf("%d",&ch);
		if(ch==1){
			int g=0;
			while(g<20){
				ans=examQuestion(ques[g],score);
				if(ans==answer[g]){
    				printf("Right");
    				score=score+1;
				}
				else{
					printf("Wrong");
					score=score-1;
				}
				g++;
			}
		}
		else{
			if(ch==2){
				printf("\n\n\nClose The Window\n\n\n");
			}
			else{
				system("cls");
				printf("\n\n\nEnter Correct Choise\n\n\n");
			}
		}
	}while(ch!=1 && ch!=2);
	return 0;
}
	
