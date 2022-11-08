cvs = [
    "I consider myself to be an epic gamer with only the finest fortnite skills",
    "I'm a highly motivated individual with at least two seconds of experience",
    "After touching my very first controller, I knew it was in my destiny to play games.",
    "I'm literally the daughter of your CEO, you're going to hire me anyways.",
    "Life isn't a game. I'm at the peak of my skills, with years of experience in the industry."
]

no_gamer_cvs = [cv for cv in cvs if "game" not in cv]
print(no_gamer_cvs)