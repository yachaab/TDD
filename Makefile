# create a make file for docker compose
DC = docker compose -f docker-compose.yml

up:
	$(DC) up -d --build
stop:
	$(DC) stop
re: stop down up
down: stop
	$(DC) down
logs:
	$(DC) logs -f
ps:
	$(DC) ps
clean:
	$(DC) down --volumes --remove-orphans
	docker images -f "dangling=true" -q | xargs -r docker rmi
fclean: stop down clean
	docker system prune -af
pytest:
	$(DC) exec -it movies pytest
makeMigrations:
	$(DC) exec -it movies python manage.py makemigrations
migrate:
	$(DC) exec -it movies python manage.py migrate
createsuperuser:
	$(DC) exec -it movies python manage.py createsuperuser
shell:
	$(DC) exec -t movies python manage.py shell
.PHONY: up stop down re clean fclean logs ps
	