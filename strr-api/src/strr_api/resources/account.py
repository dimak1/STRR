# Copyright © 2023 Province of British Columbia
#
# Licensed under the BSD 3 Clause License, (the "License");
# you may not use this file except in compliance with the License.
# The template for the license can be found here
#    https://opensource.org/license/bsd-3-clause/
#
# Redistribution and use in source and binary forms,
# with or without modification, are permitted provided that the
# following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
# 3. Neither the name of the copyright holder nor the names of its contributors
#    may be used to endorse or promote products derived from this software
#    without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS “AS IS”
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
# THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

"""
This module provides a simple flask blueprint with a single 'home' route that returns a JSON response.
"""

import logging
from http import HTTPStatus

from flasgger import swag_from
from flask import Blueprint, jsonify
from flask_cors import cross_origin

from strr_api.common.auth import jwt
from strr_api.exceptions import AuthException, ExternalServiceException, exception_response

# from strr_api.schemas import utils as schema_utils
from strr_api.services import AuthService

logger = logging.getLogger("api")
bp = Blueprint("account", __name__)


@bp.route("/me", methods=("GET",))
@swag_from({"security": [{"Bearer": []}]})
@cross_origin(origin="*")
@jwt.requires_auth
def me():
    """
    Get current user's profile.
    ---
    tags:
      - users
    responses:
      200:
        description:
      401:
        description:
    """
    try:
        token = jwt.get_token_auth_header()
        response = AuthService.get_user_accounts(token)
        profile = AuthService.get_user_profile(token)
        settings = AuthService.get_user_settings(token, profile["keycloakGuid"])
        response["profile"] = profile
        response["settings"] = settings
        return jsonify(response), HTTPStatus.OK
    except AuthException as auth_exception:
        return exception_response(auth_exception)
    except ExternalServiceException as service_exception:
        return exception_response(service_exception)


# @bp.route("/search_accounts", methods=("GET",))
# @cross_origin(origin="*")
# def search_accounts():
#     """
#     search_accounts
#     ---
#     tags:
#       - users
#     responses:
#       200:
#         description:
#       401:
#         description:
#     """

#     try:
#         token = AuthService.search_accounts("test")
#         return jsonify({"token": token}), HTTPStatus.OK
#     except AuthException as auth_exception:
#         return exception_response(auth_exception)
#     except ExternalServiceException as service_exception:
#         return exception_response(service_exception)