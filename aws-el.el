;;; aws-el.el ---

;; Copyright (C) 2015 Free Software Foundation, Inc.
;;
;; Author: Tim Hawes <Tim.Hawes@inin.com>
;; Maintainer: Tim Hawes <Tim.Hawes@inin.com>
;; Created: 03 Aug 2015
;; Version: 0.01
;; Keywords

;; This program is free software; you can redistribute it and/or modify
;; it under the terms of the GNU General Public License as published by
;; the Free Software Foundation; either version 2, or (at your option)
;; any later version.
;;
;; This program is distributed in the hope that it will be useful,
;; but WITHOUT ANY WARRANTY; without even the implied warranty of
;; MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
;; GNU General Public License for more details.
;;
;; You should have received a copy of the GNU General Public License
;; along with this program; if not, write to the Free Software
;; Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

;;; Commentary:

;;

;; Put this file into your load-path and the following into your ~/.emacs:
;;   (require 'client)

;;; Code:

(eval-when-compile
  (require 'cl))

(require 'epc)
(setq aws-dir "~/.emacs.d/programs/aws")
(defvar my-epc (epc:start-epc "python" '("/home/thawes/.emacs.d/programs/aws-el/bin/epcserver.py")))

(defun cf-validate ()
  (interactive)
  (message "%S" (epc:call-sync my-epc 'cfValidate (buffer-substring-no-properties 1 (buffer-size)))))


(defun cf-test()
  (message "%S" (epc:call-sync my-epc 'cfTest (buffer-substring-no-properties 1 (buffer-size)))))

(define-minor-mode cloudformation-mode
  "Toggle CloudFormation mode."
  :lighter " CF "
  :keymap (let ((map (make-sparse-keymap)))
            (define-key map (kbd "C-c C-c") 'cf-validate)
            map)
  :group 'cloudformation
  )

(provide 'aws-el)
;;; aws-el.el ends here
