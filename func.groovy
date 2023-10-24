def void checkout(){
  git branch:'master', url:'https://github.com/eysha-raazia/SentimentAnalysis-Flask.git'
}

def void build(){
  bat 'pip install -r requirements.txt'
}

def void deploy(){
  echo 'Deploying'
}

return this
