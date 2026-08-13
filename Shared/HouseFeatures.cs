namespace Shared;

public record HouseFeatures
{
    public required int MSSubClass { get; init; }
    public required string MSZoning { get; init; }
    public required int LotArea { get; init; }
    public required string LotShape { get; init; }
    public required string Neighborhood { get; init; }
    public required int OverallQual { get; init; }
    public required int OverallCond { get; init; }
    public required int YearBuilt { get; init; }
    public required int BedroomAbvGr { get; init; }
    public required string KitchenQual { get; init; }
}