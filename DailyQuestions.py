# -*- coding: utf-8 -*-
import datetime

QUESTIONS = [
("What Would You Like To Be Forgiven For?", "What Do You Love About Yourself?"), 
("What Achievement Have You Accomplished That Has Now Lost Its Luster?", "How Has Life Exceeded Your Expectations?"),
("Who Or What Are You Blaming?", "Who Has Made A Difference In Your Life?"),
("What Do You Say You Don't Have Time For?", "What Have You Been Learning Lately?"),
("Who Or What Have You Been Avoiding?", "What Can People Count On You For?"),
("Where Have You Broken Your Word?", " What Would You Like To Be Acknowledged For?"),
("What Do You Keep Putting Off For Another Day?", "What Do You Love About The Work You Do?"),
("What Is Your Greatest Failure?", "What Is Your Greatest Success?"),
("What Are You Holding On To But Not Relishing?", " When Do You Feel Most At Peace?"),
("What About Your Body Have You Been Making Wrong?", "What Do You Love About Your Life?"),
("What Stops You From Asking For Support?", " What Request Can You Make Today?"),
("What Do You Say Is Missing In Your Life?", " What Dream Has Come True For You?"),
("What Fear Are You Resisting Facing?", "Who Is Your Hero?"),
("Where Are You Being Right Rather Than Being Love?", "What Are You Committed To?"),
("What Are You Hiding? ", "How Can You Nurture Yourself Today?"),
("Who Do You Speak About In A Diminishing Way?", "What Is Your Contribution To The World?"),
("What Have You Been Thinking But Not Saying?", "How Do You Show Love?"),
("What Are You Afraid Of Losing?", "What Is Most Important To You?"),
("What Do You Have A Hard Time Admitting?", " What Are You Proud Of?"),
("What About Your Life Isn’t Going As Planned?", "What Energizes You?"),
("What's Bothering You?", " What Are You Grateful For?"),
]

def todaysQuestion():
	today = datetime.date.today()
	question = QUESTIONS[today.toordinal() % len(QUESTIONS)]
	return dict(first_question=question[0], second_question=question[1])