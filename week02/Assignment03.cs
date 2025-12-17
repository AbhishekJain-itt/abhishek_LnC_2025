class CustomerSearch
{
    public List<Customer> SearchByCountry(string country)
    {
        return Search(c => c.Country.Contains(country));
    }

    public List<Customer> SearchByCompanyName(string companyName)
    {
        return Search(c => c.CompanyName.Contains(companyName));
    }

    public List<Customer> SearchByContactName(string contactName)
    {
        return Search(c => c.ContactName.Contains(contactName));
    }

    private List<Customer> Search(Func<Customer, bool> predicate)
    {
        return db.customers
                 .Where(predicate)
                 .OrderBy(c => c.CustomerID)
                 .ToList();
    }

    public string ExportToCsv(List<Customer> customers)
    {
        var builder = new StringBuilder();

        foreach (var customer in customers)
        {
            builder.AppendLine(
                $"{customer.CustomerID},{customer.CompanyName},{customer.ContactName},{customer.Country}"
            );
        }

        return builder.ToString();
    }
}
