# Create your models here.

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.conf import settings



class AuditLogEntries(models.Model):
    instance_id = models.UUIDField(blank=True, null=True)
    id = models.UUIDField(primary_key=True)
    payload = models.TextField(blank=True, null=True)  # This field type is a guess.
    created_at = models.DateTimeField(blank=True, null=True)
    ip_address = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'audit_log_entries'


class Identities(models.Model):
    id = models.TextField()
    user = models.ForeignKey('Users', models.DO_NOTHING)
    identity_data = models.JSONField()
    provider = models.TextField(primary_key=True)
    last_sign_in_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth.identities'
        unique_together = (('provider', 'id'),)


class Instances(models.Model):
    id = models.UUIDField(primary_key=True)
    uuid = models.UUIDField(blank=True, null=True)
    raw_base_config = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth.instances'


class MfaAmrClaims(models.Model):
    session = models.ForeignKey('Sessions', models.DO_NOTHING)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    authentication_method = models.TextField()
    id = models.UUIDField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'auth.mfa_amr_claims'
        unique_together = (('session', 'authentication_method'),)


class MfaChallenges(models.Model):
    id = models.UUIDField(primary_key=True)
    factor = models.ForeignKey('MfaFactors', models.DO_NOTHING)
    created_at = models.DateTimeField()
    verified_at = models.DateTimeField(blank=True, null=True)
    ip_address = models.GenericIPAddressField()

    class Meta:
        managed = False
        db_table = 'auth.mfa_challenges'


class MfaFactors(models.Model):
    id = models.UUIDField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    friendly_name = models.TextField(blank=True, null=True)
    factor_type = models.TextField()  # This field type is a guess.
    status = models.TextField()  # This field type is a guess.
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    secret = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth.mfa_factors'
        unique_together = (('friendly_name', 'user'),)


class RefreshTokens(models.Model):
    instance_id = models.UUIDField(blank=True, null=True)
    id = models.BigAutoField(primary_key=True)
    token = models.CharField(unique=True, max_length=255, blank=True, null=True)
    user_id = models.CharField(max_length=255, blank=True, null=True)
    revoked = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    parent = models.CharField(max_length=255, blank=True, null=True)
    session = models.ForeignKey('Sessions', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth.refresh_tokens'


class SamlProviders(models.Model):
    id = models.UUIDField(primary_key=True)
    sso_provider = models.ForeignKey('SsoProviders', models.DO_NOTHING)
    entity_id = models.TextField(unique=True)
    metadata_xml = models.TextField()
    metadata_url = models.TextField(blank=True, null=True)
    attribute_mapping = models.JSONField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth.saml_providers'


class SamlRelayStates(models.Model):
    id = models.UUIDField(primary_key=True)
    sso_provider = models.ForeignKey('SsoProviders', models.DO_NOTHING)
    request_id = models.TextField()
    for_email = models.TextField(blank=True, null=True)
    redirect_to = models.TextField(blank=True, null=True)
    from_ip_address = models.GenericIPAddressField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth.saml_relay_states'


class SchemaMigrations(models.Model):
    version = models.CharField(primary_key=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'auth.schema_migrations'


class Sessions(models.Model):
    id = models.UUIDField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    factor_id = models.UUIDField(blank=True, null=True)
    aal = models.TextField(blank=True, null=True)  # This field type is a guess.
    not_after = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth.sessions'


class SsoDomains(models.Model):
    id = models.UUIDField(primary_key=True)
    sso_provider = models.ForeignKey('SsoProviders', models.DO_NOTHING)
    domain = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth.sso_domains'


class SsoProviders(models.Model):
    id = models.UUIDField(primary_key=True)
    resource_id = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth.sso_providers'


class SsoSessions(models.Model):
    id = models.UUIDField(primary_key=True)
    session = models.ForeignKey(Sessions, models.DO_NOTHING)
    sso_provider = models.ForeignKey(SsoProviders, models.DO_NOTHING, blank=True, null=True)
    not_before = models.DateTimeField(blank=True, null=True)
    not_after = models.DateTimeField(blank=True, null=True)
    idp_initiated = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth.sso_sessions'


class Users(models.Model):
    instance_id = models.UUIDField(blank=True, null=True)
    id = models.UUIDField(primary_key=True)
    aud = models.CharField(max_length=255, blank=True, null=True)
    role = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(unique=True, max_length=255, blank=True, null=True)
    encrypted_password = models.CharField(max_length=255, blank=True, null=True)
    email_confirmed_at = models.DateTimeField(blank=True, null=True)
    invited_at = models.DateTimeField(blank=True, null=True)
    confirmation_token = models.CharField(unique=True, max_length=255, blank=True, null=True)
    confirmation_sent_at = models.DateTimeField(blank=True, null=True)
    recovery_token = models.CharField(unique=True, max_length=255, blank=True, null=True)
    recovery_sent_at = models.DateTimeField(blank=True, null=True)
    email_change_token_new = models.CharField(unique=True, max_length=255, blank=True, null=True)
    email_change = models.CharField(max_length=255, blank=True, null=True)
    email_change_sent_at = models.DateTimeField(blank=True, null=True)
    last_sign_in_at = models.DateTimeField(blank=True, null=True)
    raw_app_meta_data = models.JSONField(blank=True, null=True)
    raw_user_meta_data = models.JSONField(blank=True, null=True)
    is_super_admin = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    phone = models.CharField(unique=True, max_length=15, blank=True, null=True)
    phone_confirmed_at = models.DateTimeField(blank=True, null=True)
    phone_change = models.CharField(max_length=15, blank=True, null=True)
    phone_change_token = models.CharField(max_length=255, blank=True, null=True)
    phone_change_sent_at = models.DateTimeField(blank=True, null=True)
    email_change_token_current = models.CharField(unique=True, max_length=255, blank=True, null=True)
    email_change_confirm_status = models.SmallIntegerField(blank=True, null=True)
    banned_until = models.DateTimeField(blank=True, null=True)
    reauthentication_token = models.CharField(unique=True, max_length=255, blank=True, null=True)
    reauthentication_sent_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth\".\"users'
# Define a default user

class Profiles(AbstractBaseUser):
    supabase_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True,null=True)
    username = models.CharField(max_length=32, unique=True)
    USERNAME_FIELD = 'username'


class Jobs(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    company_name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    salary = models.PositiveIntegerField(blank=True,null=True)
