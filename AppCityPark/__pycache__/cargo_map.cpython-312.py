�
    #�Hg#  �                   �6  � d dl mZmZmZ d dlmZ d dlmZmZ  e�       Z	 G d� de�      Z
e	j                  dej                  ��      d� �       Ze	j                  d	ej                  ��      d
efd��       Ze	j#                  dej$                  ��      de
fd��       Zy)�    )�	APIRouter�HTTPException�status)�	BaseModel)�cleverCursor�	mysqlConnc                   �"   � e Zd ZU eed<   eed<   y)�CargoDB�nombre_cargo�salarioN)�__name__�
__module__�__qualname__�str�__annotations__�int� �    �LC:\Users\Usuario\Downloads\Rest_MySQL_Fastapi_React\AppCityPark\cargo_map.pyr
   r
      s   � ����Mr   r
   z/cityPark_cargo/)�status_codec               �   �d   K  � d} t        j                  | �       t        j                  �       }|S �w)NzSelect * from cargo)r   �execute�fetchall)�selectAll_query�results     r   �	get_usersr      s,   � �� �+�O�����)��"�"�$�F��M�s   �.0z/cityPark_cargo/{cargo_id}�cargo_idc                 �~   � d}t        j                  || f�       t        j                  �       }|r|S t        dd��      �)Nz'SELECT * FROM cargo WHERE id_cargo = %si�  zCargo no encontrado�r   �detail)r   r   �fetchoner   )r   �select_queryr   s      r   �get_user_by_idr#      s=   � �<�L������{�3��"�"�$�F������4I�J�Jr   z/cityPark_crea_cargo/�	cargoPostc                 ��   � d}| j                   | j                  f}	 t        j                  ||�       t	        j
                  �        ddiS # t        j                  j                  $ r}t        dd|� ���      �d }~ww xY w)NzG
    INSERT INTO cargo (nombre_cargo, salario)
    VALUES (%s, %s)
    i�  zError: r   �messagezUser inserted successfully)	r   r   r   r   r   �commit�	connector�Errorr   )r$   �insert_query�values�errs       r   �insert_userr-      s�   � ��L� �$�$�i�&7�&7�8�F�E����\�6�2����� �3�4�4�� ���$�$� E���g�c�U�O�D�D��E�s   �*A
 �
A<�'A7�7A<N)�fastapir   r   r   �pydanticr   �Clever_MySQL_connr   r   �cargoRouterr
   �get�HTTP_302_FOUNDr   �HTTP_200_OKr   r#   �post�HTTP_201_CREATEDr-   r   r   r   �<module>r7      s�   �� 4� 4� � 5��{���i� � ���#��1F�1F��G�� H�� ���-�6�;M�;M��N�K�S� K� O�K� ���)�v�7N�7N��O�5�7� 5� P�5r   