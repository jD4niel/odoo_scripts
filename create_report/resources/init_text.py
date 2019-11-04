import os
created_by_12 = """# -*- encoding: utf-8 -*-
##################################################################################################
#
#   Author: Experts SAS (www.experts.com.mx)
#   Coded by: Daniel Acosta (daniel.acosta@experts.com.mx)
#   License: https://blog.experts.com.mx/licencia-de-uso-de-software/
#
##################################################################################################"""

created_by_10 = """#-*- coding:utf-8 -*-
#############################################################################
#    Module Writen to Odoo 10 Community Edition
#    All Rights Reserved to Experts SA de CV or Experts SAS
#############################################################################
#
#    Coded by: Daniel Acosta (daniel.acosta@experts.com.mx)
#
#############################################################################
#    This software and associated files (the "Software") can only be used
#    (executed, modified, executed after modifications) with a valid purchase
#    of these module with Experts SA de CV or Experts SAS.
#
#    You may develop Odoo modules that use this Software as a library
#    (typically by depending on it, importing it and using its resources),
#    but without copying any source code or material from the Software.
#
#    You may distribute those modules under the license of your choice,
#    provided that this license is compatible with the terms of this license.
#
#    It is forbidden to publish, distribute, sublicense, or sell copies of
#    the Software or modified copies of the Software.
#
#    The above copyright notice and this permission notice must be included in
#    all copies or substantial portions of the Software.
#
#    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
#    OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
#    THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#    THE SOFTWARE.
#############################################################################"""

def get_odoo_version():
    path = os.getcwd()
    odoov = False
    if 'odoo10' in path.split('/'):
            odoov = 10
    elif 'odoo12' in path.split('/'):
            odoov = 12
    if not odoov:
        odoov = int(input(" \nYour odoo version: "))
        while odoov not in [10,12]:
            odoov = int(input(" \nYour odoo version: "))
            if odoov not in [10,12]:
                print("\n Version de odoo no valida, utiliza 10 o 12 \n")
    return odoov

def get_module_name():
    # return current folder it means module name
    name = os.getcwd().split('/')
    return name[len(name)-1]