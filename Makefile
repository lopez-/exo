freeze:
	@pip freeze > requirements.txt

install:
	@pip install -r requirements.txt

bulid-container:
	@docker build -t exo .

container-bash:
	@docker run --rm -it -v $(pwd):/app exo /bin/bash

container-jupyter:
	@docker run --rm -it -v $(pwd):/app -p 8000:8000 exo jupyter notebook
