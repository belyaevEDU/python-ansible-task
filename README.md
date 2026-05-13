# Тестовое задание
Файлы раздела 1 находятся в папке [python](/python/).

Файлы раздела 2 находятся в корневой папке, файлы - [Dockerfile](/Dockerfile), [.dockerignore](/.dockerignore). *В задании указано, что в репозитории должно содержаться 3 директории, но docker build не позволяет копировать в образ файлы из родительских папок.*

Файлы раздела 3 находятся в папке [ansible](/ansible/).

## Python
Скрипт написан согласно ТЗ, с маленьким вопросительным моментом. В задании требуется генерировать exception при случае 4xx и 5xx кодов. При этом, при вызове скрипта, он должен выполнить 5 разных запросов. Но, если exception сгенерируется до 5го запроса и положит программу, то 5 запросов не выполнится. Как следствие, я генерирую исключение внутри собственной функции, которая отвечает за обработку статус-кодов, а уже в main функции обрабатываю исключение и логирую его.

К тому же, в задании прописано выполнять HTTP запросы к сервису [httpstat.us](https://httpstat.us), но сервис в оффлайне [из-за огромного кол-ва трафика](https://github.com/aaronpowell/httpstatus/issues/165#issuecomment-3043685050). Поэтому, я использовал [зеркало](https://tools-httpstatus.pickup-services.com/random/).

## Docker
В Ansible я использую готовый образ [belyaevedu/python-ansible-task](https://hub.docker.com/r/belyaevedu/python-ansible-task), собранный из материалов этого репозитория.

## Ansible
Для установки Docker была написана роль belyaev.script_config.docker_install, которая хранится в [ansible/collections](/ansible/collections/ansible_collections/belyaev/script_config/roles/docker_install/)

Остальные шаги прописаны в [плейбуке](/ansible/playbook.yml).