# ansible

## example command

docker run -t -v /home/ihsbramn/sandbox/ansible/ansible-nginx:/home --rm \
  -e TARGET_HOST=your-target-host \
  -e SSH_USER=your-target-username \
  -e SSH_PASS=your-target-password \
  -e SSH_PORT=your-target-port \
  syafiqizzaud/ansible-sshpass sh -c "ansible-playbook /home/nginx_install.yml -i /home/inventory.py --ssh-common-args='-o StrictHostKeyChecking=no'"
