import nltk
from nltk.chat.util import Chat, reflections

pairs=[
    [
        r"my name is (.)",
        ["Hello %1, How are you"]
    ],
    [
        r"Hi|Hello|Hey there|Heya",
        ["Hello my name is Chitti"]
    ],
    [
        r"what is your name ?",
        ["I am a chatbot created by a smart kid;)",]
    ],
    [
        r"how are you ?",
        ["I'm doing good How about You ?",]
    ],
    [
        r"sorry (.*)",
        ["Its alright","Its OK, never mind",]
    ],
    [
        r"I am fine",
        ["Great to hear that, How can I help you?",]
    ],
    [
        r"I (.*) good",
        ["Nice to hear that","How can I help you?:)",]
    ],
    [
        r"(.*) age?",
        ["I'm a now born ;N)",]
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse",]
    ],
    [
        r"(.*) created ?",
        ["A smart kid created me using Python's NLTK library!",]
    ],
    [
        r"(.*) (location|city) ?",
        ['Pune, Maharashtra',]
    ],
    [
        r"how (.*) health(.*)",
        ["I'm a computer program, so I'm always healthy ",]
    ], 
    [
        r"thanks|thank you",
        ["Happy to help",]
    ], 
    [
        r"(.*) courses to learn data science, can you suggest?",
        ["Krish Naik has many youtube videos with each step explanation along with code, you can explore!"]
    ],
    [
        r"What blogs (.*) ?",
        ["You can refer towardsdatascience, medium, analyticsvidya blogs. They are one of the great sources but you can always explore!",]        
    ],
    [
        r"(.*) algorithms?",
        ["The three machine learning types are supervised, unsupervised, and reinforcement learning. Some common algorithms are Linear regression, Logistic regression, Decision tree, SVM algorithm, Naive Bayes algorithm, KNN algorithm, K-means, Random forest algorithm",]        
    ],
     [
        r"what (.*) overfitting(.*)",
        ["The Overfitting is a situation that occurs when a model learns the training set too well, taking up random fluctuations in the training data as concepts. These impact the model’s ability to generalize and don’t apply to new data.",]
    ], 
     [
        r"how (.*) missing values(.*)",
        ["One of the easiest ways to handle missing or corrupted data is to drop those rows or columns or replace them entirely with some other value.",]
    ],
    [
        r"what is deep learning?",
        ["The Deep learning is a subset of machine learning that involves systems that think and learn like humans using artificial neural networks. The term ‘deep’ comes from the fact that you can have several layers of neural networks. "]
    ],
    [
        r"(.*) supervised learning (.*)?",
        ["Supervised learning - This model learns from the labeled data and makes a future prediction as output "]
    ],
    [
        r" (.*) unsupervised learning(.*)?",
        ["Unsupervised learning - This model uses unlabeled input data and allows the algorithm to act on that information without guidance."]
    ],
    [
        r"What (.*) bias (.*)? ",
        ["Bias in a machine learning model occurs when the predicted values are further from the actual values. Low bias indicates a model where the prediction values are very close to the actual ones."]
    ],
    [
        r"What (.*) variance (.*)? ",
        ["Variance refers to the amount the target model will change when trained with different training data. For a good model, the variance should be minimized. "]
    ],
    [
        r"what (.*) underfitting(.*)",
        ["Underfitting: High bias can cause an algorithm to miss the relevant relations between features and target outputs. "]
    ],
    [
        r"what (.*) decision tree classification(.*)",
        ["A decision tree builds classification (or regression) models as a tree structure, with datasets broken up into ever-smaller subsets while developing the decision tree, literally in a tree-like way with branches and nodes. Decision trees can handle both categorical and numerical data. "]
    ],
    [
        r"what (.*) support vectors in SVM?",
        ["A Support Vector Machine (SVM) is an algorithm that tries to fit a line (or plane or hyperplane) between the different classes that maximizes the distance from the line to the points of the classes."]
    ],
    [
        r"what (.*) bias (.*)",
        ["Bias in data tells us there is inconsistency in data. The inconsistency may occur for several reasons which are not mutually exclusive. For example, a tech giant like Amazon to speed the hiring process they build one engine where they are going to give 100 resumes, it will spit out the top five, and hire those"]
    ],
    [
        r"(.*) neural network (.*)",
        ["It is a simplified model of the human brain. Much like the brain, it has neurons that activate when encountering something similar.The different neurons are connected via connections that help information flow from one neuron to another."]
    ],
    [
        r"bye",
        ["Bye. Have a great day ahead!"]
    ],
    
]

def chat():
    print("Hey there! I am Chitti at your service")
    chat = Chat(pairs)
    chat.converse()

if __name__== "__main__":
    chat()