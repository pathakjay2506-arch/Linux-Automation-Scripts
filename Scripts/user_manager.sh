#!/bin/bash

echo "=============================="
echo "   Linux User Manager"
echo "=============================="
echo "1. Add User"
echo "2. Delete User"
echo "3. List All Users"
echo "=============================="
read -p "Choose an option (1/2/3): " choice

case $choice in
  1)
    read -p "Enter username to ADD: " username
    sudo useradd -m "$username"
    echo "✅ User '$username' created successfully."
    ;;
  2)
    read -p "Enter username to DELETE: " username
    sudo userdel -r "$username"
    echo "✅ User '$username' deleted."
    ;;
  3)
    echo "👥 All users on this system:"
    cut -d: -f1 /etc/passwd
    ;;
  *)
    echo "❌ Invalid option."
    ;;
esac