print('Hello, world!\n')
print ('test progarm ')
a= 10 ;b= 5
print('if a = 10 , b = 5 find the area of rectangle')
answer = float(input("you answer:"))
if answer == 50 :
    print ("you correct\n")
else:
    print('you r stupid'),print('area rectangle = 50,\n')
name = input("yourname:")
print("good afternoon",name,"\n\nQuiz physics exam\nStatement\n: This exam is designed to review your physics knowledge\n: this exam has 10question,10 scores\n: you can take the exam with no time limit\n: should answer as A B C D,don't full stop\n: g = 10 m/s^2")
talk = input("\nI hope you understand?:")
print("........................","\nGood Luck Your Exam\n","........................")
class Question:
     def __init__(self, prompt, answer):
          self.prompt = prompt
          self.answer = answer
question_prompts = [
     "\nQuestion1: When an object is moving at a high velocity in a fluid, it has a resistance of magnitude f=kv^2A, where v is the velocity of the object and A is the cross-sectional area. From this equation, what quantity k should be?\nA. density\nB. viscosity\nC. mass\nD. flow rate\nyour answer: ",
     "\nQuestion2: What is the unit of electrical resistivity <ρ>?\nA. Ωm\nB. Ωm^-1\nC. Ωm^-2\nD. (Ωm)^-1\nyour answer: ",
	 "\nQuestion3: How many laws in Newton,s laws of Motion?\nA. 1\nB. 2\nC. 3\nD. I don't know\nyour answer: ",
	 "\nQuestion4: An object is exerted by a force of 50 Newtons until it is accelerating 4 m/s^2, What is the mass of this object in grams?\nA. 2500\nB. 5000\nC. 10000\nD. 12500\nyour answer: ",
	 "\nQuestion5: The object and the scene are 25 cm apart. How far should a convex lens with a focal length of 6 cm be placed from the object? This will cause an image that is bigger than the object on the scene?\nA. 5\nB. 8\nC. 10\nD. 15\nyour answer: ",
	 "\nQuestion6: Pulling a mass of 1 kg from stationary to vertical with a constant force of 20 N for a distance of 5 m, how many joules of kinetic energy does an object increase in kinetic energy?\nA. 25\nB. 50\nC. 100\nD. 200\nyour answer: ",
	 "\nQuestion7: Thai national weight throwers Throwing a projectile steel ball at a speed of 20 m/s, how farthest can you throw it in meters?\nA. 10\nB. 20\nC. 30\nD. 40\nyour answer: ",
	 "\nQuestion8: A bullet 200 g with a velocity of 200 m/s was fired into a 400 g wooden plank. After the collision, it was found that the bullet penetrated the plank at a velocity of 100 m/s. How much thermal energy did this collision generate?\nA. 295 J\nB. 300 J\nC. 305 J\nD. 400 J\nyour answer: ",
	 "\nQuestion9: Which of the following affects the period of a pendulum?\nA. mass\nB. length of the string\nC. amplitude\nD. the shape of the mass on the string\nyour answer: ",
	 "\nQuestion10: What kind of wave is light?\nA. Mechanical wave\nB. UV wave\nC. longitudinal wave\nD. electromagnetic wave\nyour answer: "
]
questions = [
     Question(question_prompts[0], "A"),
     Question(question_prompts[1], "A"),
	 Question(question_prompts[2], "C"),
	 Question(question_prompts[3], "D"),
	 Question(question_prompts[4], "C"),
	 Question(question_prompts[5], "B"),
	 Question(question_prompts[6], "D"),
	 Question(question_prompts[7], "A"),
	 Question(question_prompts[8], "B"),
	 Question(question_prompts[9], "D"),
]

def run_quiz(questions):
     score = 0
     for question in questions:
          answer = input(question.prompt)
          if answer == question.answer:
               score += 1
               print("/n",name,"you got",score,len(questions))
               if score<=3:print(": your garde is D","\nYour Brain As Dog,more attentive!!!")
               elif 3<score<=6:print(": your grade is C","\nyou can Communicate in physics")
               elif 6<score<=8:print(": your grade is B","\nyou have a Big brain")
               else:print(": your garde is A","\nA god of physics")
run_quiz(questions)