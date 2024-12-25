<?php
/**
 * The base configuration for WordPress
 *
 * The wp-config.php creation script uses this file during the installation.
 * You don't have to use the website, you can copy this file to "wp-config.php"
 * and fill in the values.
 *
 * This file contains the following configurations:
 *
 * * Database settings
 * * Secret keys
 * * Database table prefix
 * * ABSPATH
 *
 * @link https://developer.wordpress.org/advanced-administration/wordpress/wp-config/
 *
 * @package WordPress
 */

// ** Database settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define( 'DB_NAME', 'wordpress' );

/** Database username */
define( 'DB_USER', 'root' );

/** Database password */
define( 'DB_PASSWORD', '' );

/** Database hostname */
define( 'DB_HOST', 'localhost' );

/** Database charset to use in creating database tables. */
define( 'DB_CHARSET', 'utf8mb4' );

/** The database collate type. Don't change this if in doubt. */
define( 'DB_COLLATE', '' );

/**#@+
 * Authentication unique keys and salts.
 *
 * Change these to different unique phrases! You can generate these using
 * the {@link https://api.wordpress.org/secret-key/1.1/salt/ WordPress.org secret-key service}.
 *
 * You can change these at any point in time to invalidate all existing cookies.
 * This will force all users to have to log in again.
 *
 * @since 2.6.0
 */
define( 'AUTH_KEY',         '`1u3x9jr1~k.xraocltKGWTWvL:kf|JpZo*zx#)<z<u~8Otd:^k@O ~{En+!c^.C' );
define( 'SECURE_AUTH_KEY',  'g,+LRBBxT(%C5q mWORQkc=LZH19}&gnUIJ_sD`Uc}#T6HOXimc8JA-?T=]`M,}T' );
define( 'LOGGED_IN_KEY',    'OeM2)S#UFR(aup=/DJ1H@Dgn=(L^/+bLeIQo9-Ngr1S=n$kztLX?@DR`jB<eG{]J' );
define( 'NONCE_KEY',        'U^arQ/&*4S9loi4hL-r7(ql{PrsX==RBMSTk,?*P5)J{h4Bys_3;l]m7?IS)_*aS' );
define( 'AUTH_SALT',        ':*?9~*y/uqp%a|BoCdb][&#3M&irFcyu(o6Y)Gi57zobNcKCmIKt 0Dyq~gv8x(X' );
define( 'SECURE_AUTH_SALT', 'qExik<F8Z.VLG85p*YU,yp!ZRUen+/PwxE/W-k}q^f- 01@,l3-9S(Oh*j;vEVt@' );
define( 'LOGGED_IN_SALT',   '=S&anocHF5K]llX1|P08X,!4_{|OzEb!4pYu{WSVc.7){hi;,B]:um.VwUKa*ghl' );
define( 'NONCE_SALT',       '_/06H7@Y>hjBb4@B0WL]B`puHa@r}I/W c)=^Mi,j<Y1@T`w?t1U_N3^qiZ)j<^P' );

/**#@-*/

/**
 * WordPress database table prefix.
 *
 * You can have multiple installations in one database if you give each
 * a unique prefix. Only numbers, letters, and underscores please!
 *
 * At the installation time, database tables are created with the specified prefix.
 * Changing this value after WordPress is installed will make your site think
 * it has not been installed.
 *
 * @link https://developer.wordpress.org/advanced-administration/wordpress/wp-config/#table-prefix
 */
$table_prefix = 'wp_';

/**
 * For developers: WordPress debugging mode.
 *
 * Change this to true to enable the display of notices during development.
 * It is strongly recommended that plugin and theme developers use WP_DEBUG
 * in their development environments.
 *
 * For information on other constants that can be used for debugging,
 * visit the documentation.
 *
 * @link https://developer.wordpress.org/advanced-administration/debug/debug-wordpress/
 */
define( 'WP_DEBUG', false );

/* Add any custom values between this line and the "stop editing" line. */



/* That's all, stop editing! Happy publishing. */

/** Absolute path to the WordPress directory. */
if ( ! defined( 'ABSPATH' ) ) {
	define( 'ABSPATH', __DIR__ . '/' );
}

/** Sets up WordPress vars and included files. */
require_once ABSPATH . 'wp-settings.php';
