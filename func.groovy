def checkout(){
  git branch:'master', url:'https://github.com/eysha-raazia/SentimentAnalysis-Flask.git'
  return this
}

def build(){
  bat 'pip install requirements.txt'
  return this
}

def deploy(){
  echo 'Deploying'
  return this
}
