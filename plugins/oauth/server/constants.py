#!/usr/bin/env python
# -*- coding: utf-8 -*-

###############################################################################
#  Copyright Kitware Inc.
#
#  Licensed under the Apache License, Version 2.0 ( the "License" );
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
###############################################################################


# Constants representing the setting keys for this plugin
class PluginSettings:
    PROVIDERS_ENABLED = 'oauth.providers_enabled'
    GITHUB_CLIENT_ID = 'oauth.github_client_id'
    GITHUB_CLIENT_SECRET = 'oauth.github_client_secret'
    GOOGLE_CLIENT_ID = 'oauth.google_client_id'
    GOOGLE_CLIENT_SECRET = 'oauth.google_client_secret'

GITHUB_AUTH_URL = 'https://github.com/login/oauth/authorize'
GITHUB_TOKEN_URL = 'https://github.com/login/oauth/access_token'
GITHUB_USER_URL = 'https://api.github.com/user'
GITHUB_EMAILS_URL = 'https://api.github.com/user/emails'
GITHUB_SCOPES = ('user:email',)

GOOGLE_AUTH_URL = 'https://accounts.google.com/o/oauth2/auth'
GOOGLE_TOKEN_URL = 'https://accounts.google.com/o/oauth2/token'
GOOGLE_USER_URL = 'https://www.googleapis.com/plus/v1/people/me'
GOOGLE_SCOPES = ('profile', 'email')
