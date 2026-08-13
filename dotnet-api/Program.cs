using System.Text.Json;
using Shared;

var builder = WebApplication.CreateBuilder(args);

// Add services to the container.
// Learn more about configuring OpenAPI at https://aka.ms/aspnet/openapi
builder.Services.AddOpenApi();

var app = builder.Build();

// Configure the HTTP request pipeline.
if (app.Environment.IsDevelopment())
{
    app.MapOpenApi();
}

app.UseHttpsRedirection();

app.MapPost("/predict", async (HouseFeatures features) =>
{
    try{
    using var httpClient = new HttpClient();
    var options = new JsonSerializerOptions { PropertyNamingPolicy = null };
    var response = await httpClient.PostAsJsonAsync("http://127.0.0.1:8000/predict", features, options);
    var result = await response.Content.ReadAsStringAsync();
    return result;
    }
    catch(Exception e)
    {
        return $"Something went wrong: {e.Message}";
    }
});

app.Run();