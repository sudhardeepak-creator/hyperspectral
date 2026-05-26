package tests;

import base.BaseTest;
import org.testng.Assert;
import org.testng.annotations.Test;
import pages.LoginPage;
import pages.ProductsPage;

public class CartTest extends BaseTest {

    @Test
    public void addToCartTest() {
        LoginPage lp = new LoginPage(driver);
        lp.login("standard_user", "secret_sauce");

        ProductsPage pp = new ProductsPage(driver);
        pp.addProduct();
        pp.openCart();

        Assert.assertTrue(driver.getCurrentUrl().contains("cart"));
    }
}