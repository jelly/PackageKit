/* -*- Mode: C; tab-width: 8; indent-tabs-mode: t; c-basic-offset: 8 -*-
 *
 * Copyright (C) 2009 Richard Hughes <richard@hughsie.com>
 *
 * Licensed under the GNU General Public License Version 2
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
 */

#if !defined (__PACKAGEKIT_H_INSIDE__) && !defined (PK_COMPILATION)
#error "Only <packagekit.h> can be included directly."
#endif

#ifndef __PK_REQUIRE_RESTART_H
#define __PK_REQUIRE_RESTART_H

#include <glib-object.h>

G_BEGIN_DECLS

#define PK_TYPE_REQUIRE_RESTART		(pk_require_restart_get_type ())
#define PK_REQUIRE_RESTART(o)		(G_TYPE_CHECK_INSTANCE_CAST ((o), PK_TYPE_REQUIRE_RESTART, PkRequireRestart))
#define PK_REQUIRE_RESTART_CLASS(k)	(G_TYPE_CHECK_CLASS_CAST((k), PK_TYPE_REQUIRE_RESTART, PkRequireRestartClass))
#define PK_IS_REQUIRE_RESTART(o)	(G_TYPE_CHECK_INSTANCE_TYPE ((o), PK_TYPE_REQUIRE_RESTART))
#define PK_IS_REQUIRE_RESTART_CLASS(k)	(G_TYPE_CHECK_CLASS_TYPE ((k), PK_TYPE_REQUIRE_RESTART))
#define PK_REQUIRE_RESTART_GET_CLASS(o)	(G_TYPE_INSTANCE_GET_CLASS ((o), PK_TYPE_REQUIRE_RESTART, PkRequireRestartClass))

typedef struct _PkRequireRestartPrivate		PkRequireRestartPrivate;
typedef struct _PkRequireRestart		PkRequireRestart;
typedef struct _PkRequireRestartClass		PkRequireRestartClass;

struct _PkRequireRestart
{
	 GObject			 parent;
	 PkRequireRestartPrivate	*priv;
};

struct _PkRequireRestartClass
{
	GObjectClass	parent_class;
	/* padding for future expansion */
	void (*_pk_reserved1) (void);
	void (*_pk_reserved2) (void);
	void (*_pk_reserved3) (void);
	void (*_pk_reserved4) (void);
	void (*_pk_reserved5) (void);
};

GType			 pk_require_restart_get_type	 	(void);
PkRequireRestart	*pk_require_restart_new			(void);

G_END_DECLS

#endif /* __PK_REQUIRE_RESTART_H */

