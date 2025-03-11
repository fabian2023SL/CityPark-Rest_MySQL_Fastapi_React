�
    ��Hg�  �                   ��  � d dl mZ d dlmZ d dlmZ d dlmZ d dlm	Z	  e�       Z
e
j                  e�       e
j                  e�       g d�Ze
j                  e	eddgdg�	�       e
j                  d
�      d� �       Ze
j                  d�      ddeedf   fd��       Ze
j                  d�      defd��       Ze
j                  d�      ddedeedf   fd��       Ze
j+                  d�      defd��       Zy)�    )�Union)�FastAPI)�usuarioRouter)�cargoRouter)�CORSMiddleware)zhttp://localhost.tiangolo.comzhttps://localhost.tiangolo.comzhttp://localhostzhttp://localhost:8080zhttp://localhost:3000T�*)�allow_origins�allow_credentials�allow_methods�allow_headers�/c               �   �   K  � ddiS �w)N�Hello�World� r   �    �GC:\Users\Usuario\Downloads\Rest_MySQL_Fastapi_React\AppCityPark\main.py�	read_rootr      s   � �� ��W����   �z/items/N�qc              �   �   K  � d| iS �w)Nr   r   )r   s    r   �read_param_itemr   !   s   � �� ���8�O�r   z/items/{item_id}�item_idc              �   �   K  � d| iS �w)Nr   r   �r   s    r   �read_paramInPath_itemr   &   s   � �� ��w���r   c              �   �   K  � | |d�S �w)N�r   r   r   r   s     r   �read_both_paramTypes_itemr   +   s   � �� ��Q�'�'�s   �z/items_del/{item_id}c              �   �   K  � ddiS �w)N�	resultadoz0Se ha eliminado correctamente el item solicitador   r   s    r   �delete_by_idr"   /   s   � �� ��K�L�L�r   )N)�typingr   �fastapir   �usuario_mapr   �	cargo_mapr   �fastapi.middleware.corsr   �app�include_router�origins�add_middleware�getr   �strr   �intr   r   �deleter"   r   r   r   �<module>r0      s1  �� � � %� !� 2��i�� � � �=� !� � � �;� ��� � � �����%��%� � � ������ �� ������U�3��9�-� � �� ���	�� ��  � � � ���	��(�S� (�U�3��9�5E� (� �(� ���"�#�M�� M� $�Mr   