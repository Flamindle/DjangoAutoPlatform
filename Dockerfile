# ��������
FROM python:3.9-slim

# ���ù���Ŀ¼
WORKDIR /app

# ���������ļ�
COPY mysite/requirements.txt .

# ��װ����
RUN pip install --no-cache-dir -r requirements.txt

# ����������Ŀ
COPY mysite/ .

# ���û�������
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=mysite.settings

# �ռ���̬�ļ������ʹ�þ�̬�ļ���
# RUN python manage.py collectstatic --noinput

# ���� gunicorn
CMD ["gunicorn", "mysite.wsgi:application", "--bind", "0.0.0.0:8000"]
