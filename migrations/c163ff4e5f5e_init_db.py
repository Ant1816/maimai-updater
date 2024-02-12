"""init db

迁移 ID: c163ff4e5f5e
父迁移: 
创建时间: 2024-02-11 18:44:27.659929

"""
from __future__ import annotations

from collections.abc import Sequence
from contextlib import suppress

import sqlalchemy as sa
from alembic import op

revision: str = "c163ff4e5f5e"
down_revision: str | Sequence[str] | None = None
branch_labels: str | Sequence[str] | None = ("maimai_updater",)
depends_on: str | Sequence[str] | None = None


def upgrade(name: str) -> None:
    with suppress(KeyError):
        globals()[f"upgrade_{name}"]()


def downgrade(name: str) -> None:
    with suppress(KeyError):
        globals()[f"downgrade_{name}"]()


def upgrade_() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade_() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def upgrade_maimai_updater() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "maimai_updater_token",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("token", sa.String(), nullable=False),
        sa.Column("userid", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_maimai_updater_token")),
        info={"bind_key": "maimai_updater"},
    )
    op.create_table(
        "maimai_updater_user",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.String(), nullable=False),
        sa.Column("friend_id", sa.String(), nullable=False),
        sa.Column("df_token", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_maimai_updater_user")),
        info={"bind_key": "maimai_updater"},
    )
    # ### end Alembic commands ###


def downgrade_maimai_updater() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("maimai_updater_user")
    op.drop_table("maimai_updater_token")
    # ### end Alembic commands ###
