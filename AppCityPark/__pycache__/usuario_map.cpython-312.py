�
    ��Ag�  �                   �   � d dl mZmZmZ d dlmZ d dlmZ  e�       Z G d� de�      Z	ej                  dej                  ��      d� �       Zy	)
�    )�	APIRouter�HTTPException�status)�	BaseModel)�cleverCursorc                   �r   � e Zd ZU eed<   eed<   eed<   eed<   eed<   eed<   eed<   eed<   eed	<   eed
<   y)�	UsuarioDB�id_usuario_Local�apellido_Local�cedula_Local�correo_electronico_Local�direccion_Local�
edad_Local�estatura_Local�nombre_Local�numero_visitas_Local�telefonoN)�__name__�
__module__�__qualname__�int�__annotations__�str� �    �NC:\Users\Usuario\Downloads\Rest_MySQL_Fastapi_React\AppCityPark\usuario_map.pyr	   r	      s<   � �������!�!����O��������Mr   r	   z/cityPark_usuarios/)�status_codec               �   �d   K  � d} t        j                  | �       t        j                  �       }|S �w)NzSelect * from usuario)r   �execute�fethall)�selectAll_query�results     r   �	get_usersr#      s,   � �� �-�O�����)��!�!�#�F��M�s   �.0N)�fastapir   r   r   �pydanticr   �Clever_MySQL_connr   �usuarioRouterr	   �get�HTTP_302_FOUNDr#   r   r   r   �<module>r*      sP   �� 4� 4� � *����
�	� 
� ���(�f�6K�6K��L�� M�r   