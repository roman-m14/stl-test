## Running with streamlit

```
$WDIR=$(pwd)
sudo docker rm streamlit ; sudo docker run -it --name streamlit --workdir $WDIR/streamlit -p 8501:8501 -v /mnt:/mnt python:3.10 bash -c 'pip install streamlit openai ; bash'

```
↓

```
cd $WDIR/test-app ; export OPENAI_KEY="....";  streamlit run app.py --server.address 0.0.0.0

```

Local: http://localhost:8501

Deploy: https://roman-m14-stl-test-app-1gp9t6.streamlit.app/

## Reference / TODO
https://blog.streamlit.io/8-tips-for-securely-using-api-keys/

https://github.com/hwchase17/langchain
