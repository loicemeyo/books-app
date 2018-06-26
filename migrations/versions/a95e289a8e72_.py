"""empty message

Revision ID: a95e289a8e72
Revises: 
Create Date: 2018-06-25 19:19:45.063664

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a95e289a8e72'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('books_book_author_key', 'books', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('books_book_author_key', 'books', ['book_author'])
    # ### end Alembic commands ###