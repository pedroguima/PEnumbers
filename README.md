# PEnumbers

Given a number, return "P" if number is divisible by 3, "E" if divisible by 5 or "PE" if divisible by 3 and 5. 
Return the number passed as argument if not divisible by 3 or 5.

The result will be given in json format.


## Build

```
docker build -t pe .
```


## Run

```
docker run -it --name=pe pe
```


## Try the online demo

```
curl https://pe.thisispedro.com/pe?number=66
```


## To do

- Automate docker build, push and deploy
- Improve in-code documentation
- Improve variable naming
- Better user validation on the API side
- Add test to check json syntax
