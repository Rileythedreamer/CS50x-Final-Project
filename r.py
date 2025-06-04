product_id_row = db.execute(
            """SELECT product_id FROM product_variants 
            WHERE id = ?
            """, product_variant_id
        )
        product_id = product_id_row[0]
        
        try:
                db.execute("""
                    DELETE FROM cart_items
                    WHERE product_variant_id IN (
                        SELECT id FROM product_variants
                        WHERE product_id = ?
                    )
                """, product_id)

                db.execute("""
                    DELETE FROM product_variants
                    WHERE product_id = ?
                """, product_id)

                db.execute("""
                    DELETE FROM products
                    WHERE id = ?
                """, product_id)

                flash("Product removed successfully", "success")
            except Exception as e:
                flash(f"Error removing product: {str(e)}", "error")

        else:
            flash("you must be logged in as owner to remove products", "error")
            return redirect("/shop")